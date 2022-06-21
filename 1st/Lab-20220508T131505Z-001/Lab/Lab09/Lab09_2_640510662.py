#!/usr/bin/env python3
# ธีรภัทร์ นิลศิริ
# 640510662
# Lab 09
# Problem 2
# 204111 Sec 002
import copy
def main():
    list_a =  [[1, 2, 3], [4], [5, 6], [7, 8, 9, 0]]

              
    row = int(input())         
    col = int(input())
    print(remove_row_col(list_a, row, col))

 
def remove_row_col(list_a, row, col):

  row_remove = []
  list_copy = copy.deepcopy(list_a)
  #positive case
  if row >= 0:
    if row <= len(list_copy):
      if row == len(list_copy):
        list_copy = copy.deepcopy(list_a)
      else:
        list_copy.pop(row)
    elif row > len(list_copy):
      list_copy = copy.deepcopy(list_a)
  #negative case
  elif row < 0 :
    if abs(row) <= len(list_copy):
      list_copy.pop(row)

    elif abs(row) > len(list_copy):
      list_copy = copy.deepcopy(list_a)


  for i in range(len(list_copy)):
  #positive case
    if col >= 0:
      if col <= len(list_copy[i]):
        col_remove = list_copy[i][:col] + list_copy[i][col+1:]
        row_remove += [col_remove]

      elif col > len(list_copy[i]):
        row_remove = list_copy

    #negative case
    elif col < 0 :
      if col <= len(list_copy[i]):
        if col == -1:
          col_remove = list_copy[i][:col] 
        else:
          col_remove = list_copy[i][:col] + list_copy[i][col+1:]
        row_remove += [col_remove]
      elif col > len(list_copy[i]):
        row_remove = list_copy
  #print((list_copy))
  #print(type(list_a))
  #print(type(row_remove))
  return row_remove

if __name__ == '__main__':
  main()
