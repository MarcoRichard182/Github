// CT018-3-1-ICP APD1F2109CS(IS)
// MARCO RICHARD PALISUAN TP062911
#include<stdio.h>
#include <string.h>
#include <stdlib.h>

void addnewtask();
void viewalltask();
void sortbydates();
void selection_sort();
void editask();
void deletetask();
int datevalidation(int dd,int mm,int yy,int *status);

typedef struct {
  char tasknames[20];
  int date;
  int month;
  int year;
  char catname[20];
  int cat_type;
  int stat_type;
  char statsname[20];
  struct{
    char taskA[10];
    char taskB[10];
    char taskC[10];
    char taskD[10];
  }cat;
  struct{
    char statA[10];
    char statB[10];
    char statC[10];
  }stat;
}task;

void addnewtask(FILE*fptr){
  int status=0;
  task tsk1;
  strcpy(tsk1.cat.taskA, "Sport");
  strcpy(tsk1.cat.taskB, "Meeting");
  strcpy(tsk1.cat.taskC, "Hometask");
  strcpy(tsk1.cat.taskD, "Hangout");
  strcpy(tsk1.stat.statA, "Scheduled");
  strcpy(tsk1.stat.statB, "Ongoing");
  strcpy(tsk1.stat.statC, "Completed");
  printf("Enter Task name:");
  scanf("%[^\n]",tsk1.tasknames);
  
  while(1){
    printf("Enter Task due dates(DD-MM-YYYY):");
    scanf("%d-%d-%d",&tsk1.date,&tsk1.month,&tsk1.year);
    datevalidation(tsk1.date,tsk1.month,tsk1.year,&status);
    if (status==1){
      break;
    }
  }
  fflush(stdin);

  while(1){
    printf("Enter Category type(1.sport 2.meeting 3.hometask 4.hangout):");
    scanf("%d",&tsk1.cat_type);
 
    if (tsk1.cat_type == 1){
      strcpy(tsk1.catname,tsk1.cat.taskA);
      break;
    }  
    else if(tsk1.cat_type == 2){
      strcpy(tsk1.catname,tsk1.cat.taskB);
      break;
    }  
    else if(tsk1.cat_type == 3){
      strcpy(tsk1.catname,tsk1.cat.taskC);
      break;
    }  
    else if (tsk1.cat_type == 4){
      strcpy(tsk1.catname,tsk1.cat.taskD);
      break; 
    }  
    else{
      printf("wrong input");
      
    }  
  }

  while(2){
    printf("Enter Your task status(1.Scheduled\n2.Ongoing\n3.Completed)\t:");
    scanf("%d",&tsk1.stat_type);
    if (tsk1.stat_type == 1){
      strcpy(tsk1.statsname,tsk1.stat.statA);
      break;
    }  
    else if(tsk1.stat_type == 2){
      strcpy(tsk1.statsname,tsk1.stat.statB);
      break;
    }  
    else if(tsk1.stat_type == 3){
      strcpy(tsk1.statsname,tsk1.stat.statC);
      break;
    }
    else{  
    printf("wrong input"); 
    }
    
  }
  fptr = fopen("siagian.txt", "a");
  fprintf(fptr, "%s;", tsk1.tasknames);
  fprintf(fptr, "%d-%d-%d;",tsk1.date,tsk1.month,tsk1.year);
  fprintf(fptr,"%s;",tsk1.catname);
  fprintf(fptr,"%s\n",tsk1.statsname);
  fclose(fptr);
};

void viewalltask(FILE*fptr){
  task tsk1;
  int choice1;
  fptr=fopen("siagian.txt","r");
  while(fscanf(fptr,"%[^;]%*c",tsk1.tasknames)!=EOF){
    fscanf(fptr,"%d%*c%d%*c%d%*c",&tsk1.date,&tsk1.month,&tsk1.year);
    fscanf(fptr,"%[^;]%*c%[^\n]%*c",tsk1.catname,tsk1.statsname);
    printf("\ntasknames:%s \t taskdates:%d-%d-%d \t category:%s\t Status:%s\n",tsk1.tasknames,tsk1.date,tsk1.month,tsk1.year,tsk1.catname,tsk1.statsname);
  }
  fclose(fptr);
  printf("Do you want to sort the file or categorize it?");
  printf("\n 1 for sort:");
  scanf("%d",&choice1);
  switch(choice1)
  {  
    case 1:
      sortbydates();
      break;
  }
}

void sortbydates(){
  FILE*fptr;
  char task_sort[80][8][80];
  task tsk1;
  int counter = 0,x,y, choice;
  fptr=fopen("siagian.txt","r");
  if (fptr == NULL) {
      printf("Error opening file \n");
      
  }
  while(2){
    printf(" 1 for asc 2 for desc\t:");
    scanf("%d",&choice);
    break;
  }
  while(fscanf(fptr,"%[^;]%*c",tsk1.tasknames)!=EOF){
    fscanf(fptr,"%d%*c%d%*c%d%*c",&tsk1.date,&tsk1.month,&tsk1.year);
    fscanf(fptr,"%[^;]%*c%[^\n]%*c",tsk1.catname,tsk1.statsname);
    strcpy(task_sort[counter][0], tsk1.tasknames);
    sprintf(task_sort[counter][1],"%02d", tsk1.date);
    sprintf(task_sort[counter][2],"%02d", tsk1.month);
    sprintf(task_sort[counter][3],"%d", tsk1.year);
    strcpy(task_sort[counter][4], tsk1.catname);
    strcpy(task_sort[counter][5], tsk1.statsname);
    counter++;      
  };
  fclose(fptr);
  for(x=0;x<counter;x++){
    for(y=0;y<=x;y++){
      int date1 = atoi (task_sort[x][1]);
      int date2 = atoi(task_sort[y][1]);
      int month1 = atoi(task_sort[x][2]);
      int month2 = atoi(task_sort[y][2]);
      int year1 = atoi(task_sort[x][3]);
      int year2 = atoi(task_sort[y][3]); 
      if (choice==1){
        if(year2>year1)
          selection_sort(task_sort,x,y);
      }    
      else{
        if (year2==year1){
        if(month2>month1)
          selection_sort(task_sort,x,y);
        else{
          if(month2==month1){
            if(date2>date1)
            selection_sort(task_sort,x,y);
          }
        }
      }
      }
      if(choice==2){  
        if(year2<year1)
          selection_sort(task_sort,x,y);
      }    
        else{
          if(year2==year1){
            if(month2<month1)
            selection_sort(task_sort,x,y);
            }
           else{
            if(month2==month1){
              if(date2<date1)
              selection_sort(task_sort,x,y);
            }
           } 
        }

    }
  }     
       
  

  
  for(x=0;x<counter;x++){
  printf("\nTasknames:%s \t Due Date:%s-%s-%s \t Category:%s Status: %s\n", task_sort[x][0], task_sort[x][1], task_sort[x][2], task_sort[x][3], task_sort[x][4], task_sort[x][5]);
  }
  };

void selection_sort (char task_sort[80][8][80], int x,int y){
  char temp[20];
  strcpy(temp,task_sort[y][5]);
  strcpy(task_sort[y][5], task_sort[x][5]);
  strcpy(task_sort[x][5], temp);
  strcpy(temp,task_sort[y][4]);
  strcpy(task_sort[y][4], task_sort[x][4]);
  strcpy(task_sort[x][4], temp);
  strcpy(temp, task_sort[y][3]);
  strcpy(task_sort[y][3],task_sort[x][3]);
  strcpy(task_sort[x][3],temp);
  strcpy(temp,task_sort[y][2]);
  strcpy(task_sort[y][2],task_sort[x][2]);
  strcpy(task_sort[x][2],temp);
  strcpy(temp,task_sort[y][1]);
  strcpy(task_sort[y][1],task_sort[x][1]);
  strcpy(task_sort[x][1],temp);
  strcpy(temp, task_sort[y][0]);
  strcpy(task_sort[y][0], task_sort[x][0]);
  strcpy(task_sort[x][0],temp);
};


void edittask(FILE*fptr){
  task tsk1;
  char taskname[20];
  int status=0,choice,flag=1;
  fptr = fopen("siagian.txt","r");
  FILE*f = fopen("tmp.txt","w");
  strcpy(tsk1.cat.taskA, "Sport");
  strcpy(tsk1.cat.taskB, "Meeting");
  strcpy(tsk1.cat.taskC, "Hometask");
  strcpy(tsk1.cat.taskD, "Hangout");
  strcpy(tsk1.stat.statA, "Scheduled");
  strcpy(tsk1.stat.statB, "Ongoing");
  strcpy(tsk1.stat.statC, "Completed");
  printf("\n Enter Taskname:");
  scanf("%[^\n]",taskname);

  while(fscanf(fptr,"%[^;]%*c ",tsk1.tasknames)!=EOF){
    fscanf(fptr,"%d%*c%d%*c%d%*c",&tsk1.date,&tsk1.month,&tsk1.year);
    fscanf(fptr,"%[^;]%*c%[^\n]%*c",tsk1.catname,tsk1.statsname);
    if(strcmp(tsk1.tasknames,taskname)==0){
      while(1){
        printf("\nUpdating -> tasknames: %s \t Taskdates: %d-%d-%d \t Category:%s Status: %s\n",tsk1.tasknames,tsk1.date,tsk1.month,tsk1.year,tsk1.catname,tsk1.statsname);
        printf("\n1. Tasknames \n");
        printf("2. Taskdates \n");
        printf("3. Category \n");
        printf("4. Status \n");
        printf("5. exit the program \n");
        printf("\nEnter your choice :");
        scanf("%d",&choice);
        fflush(stdin);
        switch(choice){
          case 1:
            printf("Enter Task name:");
            scanf("%[^\n]",tsk1.tasknames);
            flag = 1;
            break;
          case 2:
            printf("Enter Task due dates(DD-MM-YYYY):");
            scanf("%d-%d-%d",&tsk1.date,&tsk1.month,&tsk1.year);
            datevalidation(tsk1.date,tsk1.month,tsk1.year,&status);
            if (status==1){
              flag = 1;
              break;
            }
          case 3:  
            while(2){
              printf("Enter Category type(1.sport 2.meeting 3.hometask 4.hangout):");
              scanf("%d",&tsk1.cat_type);     
              if (tsk1.cat_type == 1){
                strcpy(tsk1.catname,tsk1.cat.taskA);
                flag = 1;
                break;
              }  
              else if(tsk1.cat_type == 2){
                strcpy(tsk1.catname,tsk1.cat.taskB);
                flag = 1;
                break;
              }  
              else if(tsk1.cat_type == 3){
                strcpy(tsk1.catname,tsk1.cat.taskC);
                flag = 1;
                break;
              }  
              else if (tsk1.cat_type == 4){
                strcpy(tsk1.catname,tsk1.cat.taskD);
                flag = 1;
                break; 
              }  
              else{
                printf("\nwrong input\n");
              }
            } 
          case 4:
            while(3){
              printf("Enter Your task status(1.Scheduled 2.Ongoing 3.Completed)\t:");
              scanf("%d",&tsk1.stat_type);
              if (tsk1.stat_type == 1){
                strcpy(tsk1.statsname,tsk1.stat.statA);
                flag = 1;
                break;
              }  
              else if(tsk1.stat_type == 2){
                strcpy(tsk1.statsname,tsk1.stat.statB);
                flag = 1;
                break;
              }  
              else if(tsk1.stat_type == 3){
                strcpy(tsk1.statsname,tsk1.stat.statC);
                flag = 1;
                break;
              }
              else{  
              printf("\nwrong input\n"); 
              }   
            } 
        } 
        if (flag=1){
          break;
        }               
      } 
     
      
    }
    fprintf(f,"%s;%d-%d-%d;%s;%s\n", tsk1.tasknames,tsk1.date,tsk1.month,tsk1.year,tsk1.catname,tsk1.statsname);     
 
    
  }
  fclose(fptr);
  fclose(f);
  remove("siagian.txt");  //delete old ori file
  rename("tmp.txt", "siagian.txt"); //rename the temp file to ori
}

void deletetask(){
  FILE*fptr;
  task tsk1;
  char taskname[20];
  fptr = fopen("siagian.txt","r");
  FILE*f = fopen("tmp.txt","w");
  printf("\n Enter Taskname:");
  scanf("%[^\n]",taskname);
  while(fscanf(fptr,"%[^;]%*c ",tsk1.tasknames)!=EOF){
        fscanf(fptr,"%d%*c%d%*c%d%*c",&tsk1.date,&tsk1.month,&tsk1.year);
        fscanf(fptr,"%[^;]%*c%[^\n]%*c",tsk1.catname,tsk1.statsname);
       if (strcmp(tsk1.tasknames,taskname)==0){
          continue;
       }
       fprintf(f,"%s;%d-%d-%d;%s;%s\n", tsk1.tasknames,tsk1.date,tsk1.month,tsk1.year,tsk1.catname,tsk1.statsname);
     }
       fclose(fptr);
       fclose(f);
       remove("siagian.txt");  //delete old ori file
       rename("tmp.txt", "siagian.txt"); //rename the temp file to ori
};

int datevalidation(int dd,int mm,int yy,int*status){
 if(yy>=1900 && yy<=9999)
    {
        if(mm>=1 && mm<=12)
        {
            //check days
            if((dd>=1 && dd<=31) && (mm==1 || mm==3 || mm==5 || mm==7 || mm==8 || mm==10 || mm==12)){
                printf("Date is valid.\n");
                *status=1;
            }    
            else if((dd>=1 && dd<=30) && (mm==4 || mm==6 || mm==9 || mm==11)){
                printf("Date is valid.\n");
                *status=1;
            }    
            else if((dd>=1 && dd<=28) && (mm==2)){
                printf("Date is valid.\n");
                *status=1;
            }    
            else if(dd==29 && mm==2 && (yy%400==0 ||(yy%4==0 && yy%100!=0))){
                printf("Date is valid.\n");
                *status==1;
            }    
            else{
                printf("Day is invalid.\n");
                *status=0;
            }    
        }
        else
        {
            printf("Month is not valid.\n");
            *status==0;
        }
    }
    else
    {
        printf("Year is not valid.\n");
        status==0;
    }
  
};

int main()
{
  FILE *fptr;
  int choice;
  printf("\n Hi WELCOME to Task Manager \n\n");
  while(1)
  {
      printf("\n1. Add new task \n");
      printf("2. View all task \n");
      printf("3. Update task \n");
      printf("4. Delete task \n");
      printf("5. exit the program \n");
      printf("\nEnter your choice :");
      scanf("%d",&choice);
      fflush(stdin);

      switch(choice)
      {
          case 1:
            addnewtask(fptr);
            break;

          case 2:
          viewalltask(fptr);

              break;


          case 3:
          edittask(fptr);

              break;

          case 4:
          deletetask();
              break;


          case 5:
          return 1;
          break;
      }
  }
  return 0;
}
