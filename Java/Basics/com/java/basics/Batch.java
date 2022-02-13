package com.java.basics;

public class Batch {
    public static void main(String[] args) {
      
        int diskSize = 100;
        int newDisk = diskSize;
        int diskNum = 0;
        int[] fileList = {100, 501, 30, 20, 50, 10, 10, 0};
        
        for (int index = 0; index < fileList.length; index++) {
          
          // Add 1 to the index
          //int fileAmount = index + 1;
          
          if (diskSize >= fileList[index]) {
            diskSize = diskSize - fileList[index];
          } else if (diskSize < fileList[index]) {
            
            for (int jindex = diskSize; jindex <= fileList[index]; jindex+=diskSize) {
              //diskSize = fileList[index] - diskSize;
              if (diskSize % 2 == 0) {
                diskNum = diskNum + 1;
              }
            
              //diskSize = newDisk;
            }
            
            
          }
          
          
          // Change the declaration
          if ((fileList[index]) % 2 == 0) {
                      
            diskNum = diskNum + 1;
            
            diskSize = newDisk;
            
          } 
          
        }
        if (diskSize < newDisk) {
          diskNum = diskNum + 1;
          System.out.println("Number of disks for the given files: " + diskNum);
        } else {
          System.out.println("Number of disks for the given files: " + diskNum);
        }
  
      }
}
