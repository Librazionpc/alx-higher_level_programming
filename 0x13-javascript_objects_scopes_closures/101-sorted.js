#!/usr/bin/node

const { dict } = require('./101-main.js');
const UserOccurrenceDict = [];
for (const key in dict) {
  const value = dict[key];
  if (UserOccurrenceDict[value] === undefinded) {
    UserOccurrenceDict[value] = [Key];
  }

  UserOccurrenceDict[value].push(key);
}
