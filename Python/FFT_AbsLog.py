#FFT (Log Intensity)
#This data transform takes the 3D fourier transform of a 3D dataset
#and returns the FFT's log intensity. The data is normalized such 
#that the max intensity is 1.

#WARNING: Be patient! Large datasets may take a while.

def transform_scalars(dataset):

    from tomviz import utils
    import numpy as np

    data_py = utils.get_array(dataset) 
    
    if data_py is None: #Check if data exists
        raise RuntimeError("No data array found!")

    #take log abs FFT
    data_py = np.fft.fftshift( np.log( np.abs( np.fft.fftn(data_py) ) ) )
    #normalize log abs FFT
    data_py = data_py / np.max(data_py)
    
    # set the result as the new scalars.
    utils.set_array(dataset, data_py)