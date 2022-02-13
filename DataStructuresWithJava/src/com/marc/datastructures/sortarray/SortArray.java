package com.marc.datastructures.sortarray;

public class SortArray {
    public static void main(String[] args) {
        int diskSize = 100;
        int newDisk = diskSize;
        int diskNum = 0;

        //Initialize array
        int [] fileList = new int [] {15, 3, 20, 5, 100, 1};
        int temp = 0;

        //Sort the array in descending order
        for (int i = 0; i < fileList.length; i++) {
            for (int j = i+1; j < fileList.length; j++) {
                if(fileList[i] < fileList[j]) {
                    temp = fileList[i];
                    fileList[i] = fileList[j];
                    fileList[j] = temp;
                }
            }
        }

        System.out.println();

        //Displaying elements of array after sorting
        System.out.println("Elements of array sorted in descending order: ");
        for (int index = 0; index < fileList.length; index++) {
            if (diskSize <= fileList[index]) {
                diskSize = diskSize - fileList[index];
            } else if (diskSize < fileList[index]) {
                for (int jindex = diskSize; jindex <= fileList[index]; jindex+=diskSize) {
                diskNum = diskNum + 1;
                }
            }
        }
    }
}
