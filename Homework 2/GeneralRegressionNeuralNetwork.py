#Notes
# What is tq_0, t_q, and t_i?  I will try to figure this out later..

hfs = []
t = []
dq_0 = []
sigma = 4.796

def read_feature_vectors_from_file:
    #Read feature vectors from file and append to t

def compute_outputs(t_q, t, sigma):
  for i in range(0, len(t)):
    hfs.append(hf(tq_0,t[i],sigma))   # Compute  the kernels

  for i in range(0,len(t)):
    for j in range(0,len(dq_0)):
        dq_0[i] += hfs[i]*d[i][j] #First summation Unit

  sum_hfs = 0

    for i in range(0,len(t)):
        sum_hfs += hfs[i]
        for j in range(0,3):
            dq_0[j] = dq_0[j]/sum_hfs #Output vector in decicmal form


# Euclidean Distance Squared
def dist_sqrd(t_q,t_i):
    sum = 0.0
    for i in range(0,len(t_q)):
        sum += math.pow((t_q[i] - t_i[i]),2.0)
    return sum


# Gaussian Kernel
def hf(t_q,t_i,sigma):
    return math.exp(-dist_sqrd(t_q,t_i)/pow((2.0*sigma),2.0))
