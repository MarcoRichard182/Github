#Data import

apart_dataset = read.csv("C:\\Users\\marco\\Downloads\\House_Rent_Dataset.csv", header = TRUE)



library(janitor)
library(dplyr)
library(plotrix)
library(tidyverse)
library(ggplot2)

#Data cleaning
#use to rename the table from the given excel
names(apart_dataset)=c("Posting_date", "Number_of_room", "Rent_fee","Apart_size", "Floor", "Area_type",
                       "Location", "City", "Status_of_furnishing","Preferred_tenant", "Number_of_bathroom",
                       "Contact_person")


excel_numeric_to_date(41103) #use to repair the date format from excel
"2012-08-29"

summary(apart_dataset) #use to check if there is NA or incorrect data
apart_dataset%>%is.na()%>%sum()

#Data pre-processing
View(apart_dataset)#to see the table imported
head(apart_dataset,20)#to see the top 20
tail(apart_dataset,20)#to see the last 20
names(apart_dataset)#to see the name of the columns
class(apart_dataset)#to see the data type
ncol(apart_dataset)#to see how many columns the table have
nrow(apart_dataset)#to see how many rows
summary(apart_dataset)#to see the summary of the table and the content

factor(apart_dataset$Posting_date)#to see posting date data and how many levels it have
factor(apart_dataset$Number_of_room)#to see number of room data and how many levels it have
factor(apart_dataset$Rent_fee)#to see rent fee data and how many levels it have
factor(apart_dataset$Apart_size)#to see apart size data and how many levels it have
factor(apart_dataset$Floor)#to see floor data and how many levels it have
factor(apart_dataset$Area_type)#to see area type data and how many levels it have
factor(apart_dataset$Location)#to see location data and how many levels it have
factor(apart_dataset$City)#to see city data and how many levels it have
factor(apart_dataset$Status_of_furnishing)#to see status of furnishing data and how many levels it have
factor(apart_dataset$Preferred_tenant)#to see preferred tenant data and how many levels it have
factor(apart_dataset$Number_of_bathroom)#to see number of bathroom data and how many levels it have
factor(apart_dataset$Contact_person)#to see contact person data and how many levels it have
factor(apart_dataset$Fee_per_sqft)#to see fee per sqft data and how many levels it have


#Data transformation
#to make new columns that shows fee per sqft
apart_dataset = apart_dataset %>%
  mutate(Fee_per_sqft = Rent_fee / Apart_size)
apart_dataset$Fee_per_sqft = format(round(apart_dataset$Fee_per_sqft, 2), nsmall = 2)#to make the data readble
apart_dataset$Fee_per_sqft <- as.double(apart_dataset$Fee_per_sqft)

apart_dataset$Posting_date <- as.Date(apart_dataset$Posting_date, format = "%m/%d/%Y")

#Q1 	: what determine the furnishing status 
#A1) relationship between furnishing status and BHK
ggplot(apart_dataset[apart_dataset$Number_of_room<=4,], aes(x = Number_of_room, fill = Status_of_furnishing)) + 
  geom_bar(width=0.7)+
  geom_text(stat='count',aes(label=..count..),position = position_stack(vjust = 0.5))


#A2) relationship between furnishing status and rent fee below 100000
ggplot(apart_dataset[apart_dataset$Rent_fee<=1000000 & apart_dataset$Rent_fee > 100000, ],
       aes(x = Rent_fee, y = Status_of_furnishing, col = Status_of_furnishing)) + geom_boxplot()+geom_jitter()+
  geom_text(check_overlap=TRUE,aes(label=Rent_fee))

#A3) relATionship between furnishing status and size below 2000
  summary(apart_dataset$Apart_size)
  
  ggplot(apart_dataset[apart_dataset$Apart_size<2000,],
         aes(x = Apart_size, y = Status_of_furnishing, fill = Status_of_furnishing)) + 
    geom_boxplot()+
    geom_text(size=3,check_overlap=TRUE,aes(label=Apart_size))

#A4) analyze how many there are the furnishing status
factor(apart_dataset$Status_of_furnishing)#to know what type inside status of furnishing

labels = c("Furnished", "Semi-Furnished", "Unfurnished")# 3 types inside status of furnishing
tc=apart_dataset%>%group_by(Status_of_furnishing)%>%summarise(total_count=n())#make a group by and summarise them
tc
df = data.frame(#creating data frame
  Status_of_furnishing = c("Furnished", "Semi-Furnished", "Unfurnished"),
  tc=c(680,2251,1815)
  
)
df
bepe<- ggplot(df, aes(x="", y=tc, fill=Status_of_furnishing))+
  geom_bar(width = 1, stat = "identity")+geom_text(size=3,position = position_stack(vjust = 0.5),aes(label=tc))
bepe
pie <- bepe + coord_polar("y", start=0)#making pie chart
pie+labs(title="Number of apartment furnishing status")#give title to the pie chart

#A5) relationship between furnishing status and city
ggplot(apart_dataset,aes(x=City, fill=City))+geom_histogram(stat = "count")+
  facet_wrap(~Status_of_furnishing)+ geom_text(stat='count',position=position_stack(vjust = 0.5),aes(label=..count..))
  
#A6) relationship between furnishing status and tenant preferred
ggplot(apart_dataset,aes(x=Preferred_tenant, fill=Status_of_furnishing))+geom_bar()+
  geom_text(stat='count',position=position_stack(vjust = 0.5),aes(label=..count..))
  

#A7) relationship between furnishing status and bathroom
ggplot(apart_dataset,aes(x=Number_of_bathroom,fill=Status_of_furnishing, y=Status_of_furnishing))+geom_violin()+
  geom_text(aes(label=Number_of_bathroom))

#A8) relation ship between furnishing status and point of contact
ggplot(apart_dataset, aes(x = Contact_person, fill = Contact_person)) + 
  geom_bar()+
  geom_text(stat='count',position=position_stack(vjust = 0.5), aes(label=..count..))+
  facet_wrap(~Status_of_furnishing)

#A9) Relationship between furnishing status and Area type
ggplot(apart_dataset, aes(x = Area_type, fill = Area_type)) + 
  geom_bar()+
  geom_text(stat='count', aes(label=..count..))+
  facet_wrap(~Status_of_furnishing)

#A10) Relationship between furnishing status and fee per square
summary(apart_dataset$Fee_per_sqft)
ggplot(apart_dataset[apart_dataset$Fee_per_sqft<85, ],
       aes(x = Fee_per_sqft, y = Status_of_furnishing, fill = Status_of_furnishing)) + geom_violin()+geom_boxplot()

#A11) relationship between furnishing status and posting Date
ggplot(apart_dataset,aes(x=Posting_date,fill=Status_of_furnishing)) + 
  geom_histogram(stat = "bin", bins = 10,position = "dodge")

#Q2. Find apartment that suits for family
#A1)  analyze BHK that suits for family 
ggplot(apart_dataset[apart_dataset$Preferred_tenant=="Family",],
       aes( x = Number_of_room)) + 
  geom_histogram(colour="orange",aes(fill=..count..))+
  scale_fill_gradient("count",low="purple",high="blue")


#A2) analyze rent fee suits for family
ggplot(apart_dataset[apart_dataset$Preferred_tenant=="Family"& apart_dataset$Rent_fee<=23000,],
       aes(x = Rent_fee,fill=City, y = City)) + 
  geom_boxplot()

#A3)analyze size of apartment that suits for family

ggplot(apart_dataset[apart_dataset$Preferred_tenant=="Family",],
       aes( x = Apart_size)) + 
  geom_histogram(colour="orange",aes(fill=..count..))+
  scale_fill_gradient("count",low="purple",high="blue")

#A4) analyze area type of apartment that suits for family
ggplot(apart_dataset[apart_dataset$Preferred_tenant=="Family",],
       aes( x = Area_type)) + 
  geom_bar(colour="orange",aes(fill=..count..))+
  scale_fill_gradient("count",low="purple",high="blue")+
  geom_text(stat='count',aes(label=..count..),position = position_stack(vjust = 0.5))

#A5)  analyze city of apartment that suits for familty
ggplot(apart_dataset[apart_dataset$Preferred_tenant=="Family",],
       aes( x = City)) + 
  geom_bar(colour="orange",aes(fill=..count..))+
  scale_fill_gradient("count",low="yellow",high="red")+
  geom_text(stat='count',aes(label=..count..),position = position_stack(vjust = 0.5))

#A6)analyze furnishing status of apartment that suits for family
ggplot(apart_dataset[apart_dataset$Preferred_tenant=="Family",],
       aes( x = Status_of_furnishing)) + 
  geom_bar(colour="orange",aes(fill=..count..))+
  scale_fill_gradient("count",low="red",high="blue")+
  geom_text(stat='count',aes(label=..count..),position = position_stack(vjust = 0.5))

#A7) analyze bathroom that suits for family
ggplot(apart_dataset[apart_dataset$Preferred_tenant=="Family",],
       aes( x = Number_of_bathroom)) + 
  geom_bar(colour="orange",aes(fill=..count..))+
  scale_fill_gradient("count",low="purple",high="orange")+
  geom_text(stat='count',aes(label=..count..),position = position_stack(vjust = 0.5))

#8) analyse the contact person that suits for family
ggplot(apart_dataset[apart_dataset$Preferred_tenant=="Family",],
       aes( x = Contact_person)) + 
  geom_bar(colour="orange",aes(fill=..count..))+
  scale_fill_gradient("count",low="red",high="blue")+
  geom_text(stat='count',aes(label=..count..),position = position_stack(vjust = 0.5))
apart_dataset$Fee_per_sqft<85
#9) analyse the fee per square feet person that suits for family
ggplot(apart_dataset[apart_dataset$Fee_per_sqft<85&apart_dataset$Preferred_tenant=="Family", ],
       aes(x = Fee_per_sqft, y = Status_of_furnishing, fill = Status_of_furnishing)) + geom_violin()

#10)analyse the posting date that the apartment for family got posted
ggplot(apart_dataset[apart_dataset$Preferred_tenant=="Family",],
       aes( x = Posting_date)) + 
  geom_bar(colour="orange",aes(fill=..count..))+
  scale_fill_gradient("count",low="red",high="blue")+
  geom_text(stat='count',aes(label=..count..),position = position_stack(vjust = 0.5))

#Q3) Find the apartment that cost below 10000 and the apartment size is 3000
#1) analyse apartment that cost below 10000 and the apartment size is 3000 using scatterplot
ggplot(apart_dataset[apart_dataset$Rent_fee<10000& apart_dataset$Apart_size<3000, ],
       aes(x = Apart_size, y = Rent_fee, col = Status_of_furnishing)) + geom_point(aes(color=Rent_fee))

#2)analyse apartment that cost below 5000 and the apartment size is 1000 using line graph
ggplot(apart_dataset[apart_dataset$Rent_fee<5000& apart_dataset$Apart_size<1000, ],
       aes(x = Apart_size, y = Rent_fee, col = Status_of_furnishing)) + geom_line(aes(color=Rent_fee))





