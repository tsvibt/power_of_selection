import numpy as np
import mpmath
import statistics
from scipy.integrate import quad

#exec(open('stats.py').read())

def length_variance(l):
   return l/4

def length_SD(l):
   return np.sqrt(length_variance(l))

def length_mean(l):
   return l/2

def division_variance(divisions):
   return 1/np.sqrt(divisions)

#could speed up slightly by pre-initializing but whatever:
#StandardNormal = statistics.NormalDist(sigma=1, mu=0)

def gaussian_pdf(sigma, mu, x):
   return statistics.NormalDist(sigma=sigma, mu=mu).pdf(x)

def gaussian_cdf(sigma, mu, x):
   return statistics.NormalDist(sigma=sigma, mu=mu).cdf(x)

def gaussian_inv_cdf(sigma, mu, x):
   return statistics.NormalDist(sigma=sigma, mu=mu).inv_cdf(x)

def gaussian_max_cdf(sample_count, sigma, mu, x):
   return gaussian_cdf(sigma, mu, x)**(sample_count)

def gaussian_max_pdf(sample_count, sigma, mu, x):
   return sample_count * gaussian_pdf(sigma, mu, x) * gaussian_cdf(sigma, mu, x)**(sample_count -1)

def gaussian_max_median(sample_count, sigma, mu):
   return gaussian_inv_cdf(sigma, mu, (1/2)**(1/(sample_count)))

def gaussian_max_numerical(sample_count, sigma, mu):
   res, _ = quad(lambda x: x*gaussian_max_pdf(sample_count, 1, 0, x), -np.inf, np.inf)
   return sigma*res+mu

def gaussian_max_sample(sample_count, sigma, mu):
   return np.max(np.random.normal(loc=mu, scale=sigma, size=int(sample_count)))

def second_largest(xs):
   return np.partition(xs, -2)[-2]

def gaussian_secondmax_sample(sample_count, sigma, mu):
   return second_largest(np.random.normal(loc=mu, scale=sigma, size=int(sample_count)))

def gaussian_firstsecondmax_sample(sample_count, sigma, mu):
   sample = np.random.normal(loc=mu, scale=sigma, size=int(sample_count))
   return np.max(sample) + second_largest(sample)


# n(n-1) ϕ(x) [Φ(x)^{n-2}-Φ(x)^{n-1}]
def gaussian_secondmax_pdf(sample_count, sigma, mu, x):
   return (sample_count * (sample_count - 1) * gaussian_pdf(sigma, mu, x)* 
         (gaussian_cdf(sigma, mu, x)**(sample_count-2) - gaussian_cdf(sigma, mu, x)**(sample_count-1)))

# (1-n) Φ(x)^n + nΦ(x)^{n-1}
def gaussian_secondmax_cdf(sample_count, sigma, mu, x):
   return ((1 - sample_count) * gaussian_cdf(sigma, mu, x)**sample_count + 
         sample_count * gaussian_cdf(sigma, mu, x)**(sample_count-1))

def gaussian_secondmax_numerical(sample_count, sigma, mu):
   res, _ = quad(lambda x: x*gaussian_secondmax_pdf(sample_count, 1, 0, x), -np.inf, np.inf)
   return sigma*res+mu

def gaussian_firstsecondmax_numerical(sample_count, sigma, mu):
   return gaussian_max_numerical(sample_count, sigma, mu) + gaussian_secondmax_numerical(sample_count, sigma, mu)

def odds_SDs(out_of, sigma=1):
   return gaussian_inv_cdf(sigma, 0, (out_of-1)/out_of) / sigma

def SD_odds(sd):
   return "e" + str(round(np.log10(1/(1-gaussian_cdf(1, 0, sd))), 2))


