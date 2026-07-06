'''
Data Binning Tool
Binglu Wang 02/02/2018
Based on Yian Yin's code
'''
import numpy as np
import math

def linear_binning(k,num):
    #k is the result to be binned, and num is the number of binning
    if k == []:
        print("Warning! sequence empty!")
        bin_mid = 0
        bin_num = 0
    else:
        max_x = max(k)+0.01
        min_x = min(k)
        step = float(max_x-min_x)/float(num)
        t = np.arange(min_x,max_x,step)
        t=list(t)
        t.append(max_x)
        bin_num=[]
        bin_mid=[]
        for i in range(0,len(t)-1):
            lower_bound = t[i]
            upper_bound = t[i+1]
            #bin_mid.append(0.5*(lower_bound+upper_bound))
            #bin_mid.append(lower_bound)
            bin_length = upper_bound-lower_bound
            data_bin = [j for j in k if j >= lower_bound and j < upper_bound]
            if data_bin == []:
                continue
            bin_num.append(float(len(data_bin))/len(k)/bin_length)
            bin_mid.append(float(sum(data_bin))/len(data_bin))
            if bin_num[-1] <= 10**(-16) :
                del bin_mid[-1]
                del bin_num[-1]
    return bin_mid, bin_num

def log_binning(k,num):
    if k == []:
        print("Warning! sequence empty!")
        bin_mid = 0
        bin_num = 0
    else:
        max_x = math.log(max(k)+0.01,2)
        min_x = math.log(min(k),2)
        step = float(max_x-min_x)/float(num)
        t = np.arange(min_x,max_x,step)
        t=list(t)
        t.append(max_x)
        bin_num=[]
        bin_mid=[]
        for i in range(0,len(t)-1):
            lower_bound = 2**t[i]
            upper_bound = 2**t[i+1]
            bin_length = upper_bound-lower_bound
            data_bin = [j for j in k if j >= lower_bound and j < upper_bound]
            if data_bin == []:
                continue          
            bin_num.append(float(len(data_bin))/len(k)/max(1.0,bin_length))
            bin_mid.append(float(sum(data_bin))/len(data_bin))
            if bin_num[-1] <= 10**(-16) :
                del bin_mid[-1]
                del bin_num[-1]
    return bin_mid, bin_num

def linear_binningtwo(xs,ys,num):
    #k is the result to be binned, and num is the number of binning
    if len(xs) == 0:
        print("Warning! sequence empty!")
        bin_mid = 0
        bin_num = 0
    
    else:
        max_x = max(xs)+0.01
        min_x = min(xs)
        step = float(max_x-min_x)/float(num)
        t = np.arange(min_x,max_x,step)
        t=list(t)
        t.append(max_x)
        bin_num=[]
        bin_mid=[]
        for i in range(0,len(t)-1):
            lower_bound = t[i]
            upper_bound = t[i+1]
            #bin_mid.append(0.5*(lower_bound+upper_bound))
            #bin_mid.append(lower_bound)
            bin_length = upper_bound-lower_bound
            data_bin = [ys[j] for j in range(len(xs)) if xs[j] >= lower_bound and xs[j] < upper_bound]
            if data_bin == []:
                continue
            bin_num.append(float(np.mean(data_bin)))
            bin_mid.append(float(lower_bound+upper_bound)/2)
            if bin_num[-1] <= 10**(-16) :
                del bin_mid[-1]
                del bin_num[-1]
    return bin_mid, bin_num

def log_binningtwo(xs,ys,num):
    #k is the result to be binned, and num is the number of binning
    if len(xs) == 0:
        print("Warning! sequence empty!")
        bin_mid = 0
        bin_num = 0
    
    else:
        max_x = math.log(max(xs)+0.01,2)
        min_x = math.log(min(xs),2)
        step = float(max_x-min_x)/float(num)
        t = np.arange(min_x,max_x,step)
        t=list(t)
        t.append(max_x)
        bin_num=[]
        bin_mid=[]
        for i in range(0,len(t)-1):
            lower_bound = 2**t[i]
            upper_bound = 2**t[i+1]
            #bin_mid.append(0.5*(lower_bound+upper_bound))
            #bin_mid.append(lower_bound)
            bin_length = upper_bound-lower_bound
            data_bin = [ys[j] for j in range(len(xs)) if xs[j] >= lower_bound and xs[j] < upper_bound]
            if data_bin == []:
                continue
            bin_num.append(float(np.mean(data_bin)))
            bin_mid.append(float(lower_bound+upper_bound)/2)
            if bin_num[-1] <= 10**(-16) :
                del bin_mid[-1]
                del bin_num[-1]
    return bin_mid, bin_num