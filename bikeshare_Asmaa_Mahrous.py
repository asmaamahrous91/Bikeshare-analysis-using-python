import pandas as pd
import numpy as np
import time



CITY_DATA = { 'ch': 'chicago.csv',
              'ny': 'new_york_city.csv',
              'wa': 'washington.csv' }
day_data={'1':'Saturday','2':'Sunday','3':'Monday',
           '4':'Tuesday','5':'Wednesday','6':'Thursday',
           '7':'Friday','0':'no filter'}
month_list={'1':'January','2':'Febrauary','3':'March',
           '4':'April','5':'May','6':'June'}
city_list=['NY','CH','WA']

def city_check():
    city=''
    while city.upper() not in city_list:
        city=input("Please Tell us which city you wanna to see data for it:New York City(NY) or Chicago(CH) or Washington(WA)")
        print(city)

    return city

def month_check():

    while True:
        month_str=input("Select the prefered month please insert it as intger (you can enter 0 if no month filter needed):- 1,2, 3, 4, 5, 6?") 
        if month_str.strip().isdigit():
            month_2=int(month_str)
            if month_2 in range(0,7):
                month=month_2
                #print(type(month))
                #print(month)
                break
    return month

def day_check():
    while True:
        day_str=input("Select the prefered Day please insert it as intger (you can enter 0  if no day filter needed):-\n 1- Saturday ,2- Sunday,.....,7- Friday ?") 
        if day_str.strip().isdigit():
            day_2=int(day_str)
            if day_2 in range(0,8):
                day=day_2
                #print(type(day))
                #print(day)
                break

    return day


def filter_data_input(city,month,day):
    print("function start")
    month=str(month)
    
    city=str(city)
    
    file_name= CITY_DATA.get(city.lower())
    
    data = pd.read_csv(file_name)
    data_all=data
    data['Start Time'] = pd.to_datetime(data['Start Time'])
    data['Month']= data['Start Time'].dt.month
    
    data_month_filtered= data[data['Month'] == int(month)]
    
    
    day=str(day)
    day_name=day_data.get(day)
    city=str(city)
    
    if int(month) in range(1,7):
        data= data_month_filtered
        
    else:  
        file_name= CITY_DATA.get(city.lower())
        data = pd.read_csv(file_name)
    
        
    
    data['Start Time'] = pd.to_datetime(data['Start Time'])
   
    data['Day']= data['Start Time'].dt.day_name()
         
    data_day_filtered=data[data['Day'].values == day_name.title()]
    data_month_day_filtered=data_day_filtered
    df=data_month_day_filtered
   
    if int(day) == 0 and int(month) in range(1,7):
        
        df= data_month_filtered
        return df
    elif int(month)==0 and int(day) in range(1,8):
        df= data_day_filtere
        
        return df
    elif int(day) ==0 and int(month)==0:
            file_name= CITY_DATA.get(city.lower())
            data = pd.read_csv(file_name)
            df= data

            return df
    else:
        return df
    
  
    
def get_common_times(city):
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time=time.time()
    city=str(city)
    file_name= CITY_DATA.get(city.lower())
    df = pd.read_csv(file_name)
    data=df
    data['Start Time'] = pd.to_datetime(data['Start Time'])
        # extract month and day from the Start Time column to create new columns
    data['Month']= data['Start Time'].dt.month
    data['Day']= data['Start Time'].dt.day_name()

    common_month=df['Month'].mode()[0]
    
    trip_tot=df[df['Month']==common_month]
    trip_tot=trip_tot['Trip Duration'].sum()
    trip_tot_hh=trip_tot/(60*60)
    
    print('Most Common Month is {} with Total Trip duration {} seconds ({} hours).'.format(common_month,trip_tot
                                                                                           ,int(trip_tot_hh)))
    
    common_day=df['Day'].mode()[0]
     
    trip_avg=df[df['Day']==common_day]
    trip_avg=trip_avg['Trip Duration'].mean()
    trip_avg_mm=trip_avg/60
    print('Most Common Day is {} with AVG. Trip duration {} seconds ({} Minutes).'.format(common_day,trip_avg,trip_avg_mm))
    
    df['Hour']= df['Start Time'].dt.hour
    common_hour=df['Hour'].mode()[0]
    if common_hour >12:
        df['Frequent Time']= df['Start Time'].dt.time
        frequent_time= df['Frequent Time'].mode()[0]
        print("Most Common Hour:{} P.M.".format(int(common_hour)-12))
        print("The Most Frequent Time of Travel is {}.".format(frequent_time))
    else:
        df['Frequent Time']= df['Start Time'].dt.time
        frequent_time= df['Frequent Time'].mode()[0]
        print("Most Common Hour:{} A.M.".format(int(common_hour)))
        print("The Most Frequent Time of Travel is {}.".format(frequent_time))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    

    


def station_stats(df):
    start_time=time.time()
    
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    
    df['Start']= df['Start Station']
    start_Common= df.mode()['Start'][0]
    df['End']= df['End Station']
    end_Common= df.mode()['End'][0]
    
    most_frequent=df[df['Start Station']==start_Common]
    most_frequent_end= df[df['End Station']==end_Common]
    most_frequent_count=len(most_frequent)
    most_frequent=most_frequent.head(1)
    
    print("Most Common Satrt Station is: ",start_Common)
    print("Most Common Destinantion is ",end_Common)
    
    print("Most Frequent Trip starts from {} and ends at {} and it took {} Seconds and it Repeated for {} Times during First 6 Month of 2017.".format(most_frequent['Start'].values
                                                                          ,most_frequent['End'].values,most_frequent['Trip Duration'].values,most_frequent_count))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)




def user_stats(df,city):
    
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()
    subscriber_count=df[df['User Type']=='Subscriber']
       
    subscriber_count= subscriber_count['User Type'].count()
    
    customer_count=df[df['User Type']=='Customer']
       
    customer_count= customer_count['User Type'].count()
    print("Regarding the Previous mentioned common times the breakdown of users types was the following:\n *Subscriber:- {}\n *Customer:{}".format(subscriber_count,customer_count))
   
    
    
    if city.lower()!="wa":
        erlist_age=df['Birth Year'].min()
        #print(erlist_age,"\n")
        recent_age=df['Birth Year'].max()
        #print(recent_age,"\n")
        common_birth_year=df['Birth Year'].mode()[0]
        #print(common_birth_year,"\n")
        youngest=2017-int(recent_age)
        oldest=2017-int(erlist_age)
        popular=2017-int(common_birth_year)
        print('-'*10)
        print("Regarding the Previous mentioned common times the breakdown of users ages at 2017 was the following:\n *Oldest:- {}\n *Youngest:{}\n*Popular age:{}".format(oldest
        ,youngest,popular))

    else:
        print('-'*5)
        print("No Age Data")
    
    if city.lower()!="wa":
        males=df[df['Gender']=='Male']
        males_count= males['Gender'].count()
        #print(males_count,"\n")
        females=df[df['Gender']=='Female']
        females_count= females['Gender'].count()
        print('-'*5)
        print("Regarding the Previous mentioned common times the breakdown of users Gender was as the following:\n *Female:- {}\n *Male:-{}".format(females_count,males_count))
  
        #print(females_count,"\n")


    else:
        print('-'*5)
        print("No Gender Data")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    i=0
    while True:
        city= city_check()
        month=month_check()
        day= day_check()
        df=filter_data_input(city,month,day)
        
        get_common_times(city)
        station_stats(df)      
        user_stats(df,city)
        while True:
            disply_data = input('\n Would you like to disply the Data you filtered? Enter yes or no.\n')
            i+=5
            if disply_data.lower() != 'yes':
                break
            else:          
                if int(day) ==0 and int(month)==0:
                    print("here is the first 5 Raws in the file for the selected City:\n",df.head(i))
                else:  
                    print("here is the first 5 Raws filtered by your selctions:\n",df.head(i))
                

        
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
