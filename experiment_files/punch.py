"""Base experiment definition for punch project. Only contains preproc info."""
source_template = "{subject_id}/bold/functional_??.nii.gz"
whole_brain_template = "{subject_id}/bold/whole_brain_EPI.nii.gz"
n_runs = 12
TR = 2
frames_to_toss = 6
temporal_interp = True
interleaved = True 
slice_order = "up"
intensity_threshold = 5
motion_threshold = .5
spike_threshold = -10
smooth_fwhm = 4
hpf_cutoff = 128
