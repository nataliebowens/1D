// http://www.me.ucsb.edu/~moehlis/APC591/tutorials/tutorial5/node3.html

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <iomanip>
#include <omp.h>

using std::cout;
using std::endl;
using std::string;
using std::ostringstream;
using std::ofstream;
using std::setw;
using std::setfill;

const int Numx = 100;
const int Numy = 50;
const double Lx = 2.0;
const double Ly = 1.0;

double dt;
double dx;
double dy;
double dx2;
double dy2;
double lamx;
double lamy;
double lam;

double **phi;
double **newphi;

/////////////////////////////////////
/////////////////////////////////////

void PrintPhi(ofstream *fileOut) {
    // for gnuplot

    for (int i=0; i<Numy; i++) {
        for (int j=0; j<Numx; j++)
            *fileOut << setw(15) << j*dx << setw(15) << i*dy << setw(15) << phi[i][j] << endl;
        *fileOut << setw(15) << Numx*dx << setw(15) << i*dy << setw(15) << 0 << endl;
        *fileOut << endl;
    }

    for (int j=0; j<Numx; j++)
        *fileOut << setw(15) << j*dx << setw(15) << Numy*dy << setw(15) << 0 << endl;

    *fileOut << setw(15) << Numx*dx << setw(15) << Numy*dy << setw(15) << 0 << endl;
    *fileOut << endl << endl;
}


void SetBoundary(double **data) {

    for (int i=0; i<Numx; i++) {
        data[0][i]      = dx*i;
        data[Numy-1][i] = dx*i;
    }

    for (int i=0; i<Numy; i++) {
        data[i][0]      = 0;
        data[i][Numx-1] = dx*(Numx-1);
    }
}


void Evolve(const int N) {

    double **tmp;

    for (int n=0; n<N; n++) {
        #pragma omp parallel for
        for (int i=1; i<Numy-1; i++)
            for (int j=1; j<Numx-1; j++)
                newphi[i][j] = lamx*(phi[i][j-1] + phi[i][j+1]) +
                               lamy*(phi[i-1][j] + phi[i+1][j]) +
                               lam * phi[i][j];
        tmp = phi;
        phi = newphi;
        newphi = tmp;
    }
}


void PrepAnim(const int ncycles, const int nsteps, const string filename) {

    ofstream fileOut(filename.c_str());

    PrintPhi(&fileOut);
    for (int i=0; i<ncycles; i++) {
        Evolve(nsteps);
        PrintPhi(&fileOut);
        cout << i << endl;
    }

    fileOut.close();
}


//////////////////////////////////////
//////////////////////////////////////

void Init() {

    // allocate and zero storage arrays
    phi    = new double *[Numy];
    newphi = new double *[Numy];
    for (int i=0; i<Numy; i++) {
        phi[i]    = new double[Numx];
        newphi[i] = new double[Numx];
        for (int j=0; j<Numx; j++) {
            phi[i][j]    = 0;
            newphi[i][j] = 0;
        }
    }

    dx   = Lx / Numx;
    dy   = Ly / Numy;
    dx2  = dx * dx;
    dy2  = dy * dy;
    dt   = 0.5 * dx2 * dy2 / (dx2 + dy2);
    lamx = dt / dx2;
    lamy = dt / dy2;
    lam  = -2 * (lamx + lamy - 0.5);

    cout << "Simple heat conduction using OpenMP\n";
    #pragma omp parallel
    #pragma omp single
        cout << "# of procs: " << omp_get_num_threads() << endl << endl;

    SetBoundary(phi);
    SetBoundary(newphi);
}


void Run() {
    PrepAnim(250, 10, string( "animdata.txt"));
}


void CleanUp() {
    for (int i=0; i<Numy; i++) {
        delete phi[i];
        delete newphi[i];
    }
    delete phi;
    delete newphi;
}


int main() {
    Init();
    Run();
    CleanUp();
    return 0;
}

