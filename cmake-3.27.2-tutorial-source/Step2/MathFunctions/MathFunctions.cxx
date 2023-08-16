#include "MathFunctions.h"

// TODO 11: include cmath
#include "cmath"

// TODO 10: Wrap the mysqrt include in a precompiled ifdef based on USE_MYMATH
// #include "mysqrt.h"


namespace mathfunctions {
double sqrt(double x)
{
  #ifdef USE_MYMATH
    return detail::mysqrt(x);
  #else
    return std::sqrt(x);
  #endif
}
}
