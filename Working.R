LongData <-read.csv("NFLKickReturnQuery.csv")

library(reticulate)
#py_install("pandas")
import("pandas")
source_python("Metrica_IO.py")
source_python("myversion_Metric_PitchControl.py")

library(tidyverse)
widedata <- LongData %>% select(combid, Name, x,y) %>%
  pivot_wider(names_from = Name, values_from = c(x,y))%>%
  setNames(nm = sub("(.*)_(.*)_(.*)", "\\2_\\3_\\1", names(.))) %>% select(-c(Def_11_x,Def_11_y ))

PossTeams<-widedata %>% select(combid:Poss_11_x, Poss_1_y:Poss_11_y)
DefTeams<-widedata %>% select(combid,Def_12_x:Def_22_x,Def_12_y:Def_22_y)
write.csv(PossTeams, "PossTeams.csv")
write.csv(DefTeams, "DefTeams.csv")

speed_widedata <- LongData %>% select(combid, Name, s) %>%
  pivot_wider(names_from = Name, values_from = s)%>%
   select(-Def_11)
write.csv(speed_widedata, "speed_widedata.csv")
