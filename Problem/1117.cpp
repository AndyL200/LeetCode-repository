#include <functional>
#include <mutex>
#include <condition_variable>
using namespace std;
class H2O {
private:
    mutex mtx;
    condition_variable cv;
    int hydrogen_count = 0;
public:
   
    H2O() {
    }

    void hydrogen(function<void()> releaseHydrogen) {
        unique_lock<mutex> lock(mtx);

        while (hydrogen_count >= 2) {
            cv.wait(lock);
        }

        hydrogen_count++;
        // releaseHydrogen() outputs "H". Do not change or remove this line.
        releaseHydrogen();

        cv.notify_one();
        
    }

    void oxygen(function<void()> releaseOxygen) {
        unique_lock<mutex> lock (mtx);

        while (hydrogen_count < 2) {
            cv.wait(lock);
        }
        // releaseOxygen() outputs "O". Do not change or remove this line.
        releaseOxygen();

        hydrogen_count = 0;

        //More than one hydrogen thread
        cv.notify_all();
        }
};