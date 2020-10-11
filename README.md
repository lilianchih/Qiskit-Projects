# Spin Squeezing Optimization

  The program "spin_squeezing.py" aims to optimize a sequence of quatnum gates applied to neutral atoms in an optical tweezer array in order to generate spin-squeezed states. Spin squeezed states are important sources for quantum metrology, since they have reduced variance in certain directions, and enable sensing at the Heisenberg limit.
  The metric for optimization is the Wineland spin-squeezing parameter, which is defined as
  $\xi^2 = N\frac{(\Delta J_{\perp,min})^2}{|J|^2}\,.$ The Nelder-Mead method is used to optimize the gate sequence. The Qiskit package by IBM-Q is used to simulate the quantum circuit.
  Preliminary results show that the squeezing parameter is reduced by 2 orders of magnitude.


