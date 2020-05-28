LongData <-read.csv("NFLKickReturnQuery.csv")

library(reticulate)
#py_install("pandas")
import("pandas")
source_python("Metrica_IO.py")
source_python("myversion_Metric_PitchControl.py")
