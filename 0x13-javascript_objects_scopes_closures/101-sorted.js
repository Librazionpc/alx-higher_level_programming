#!/usr/bin/node

const { dict } = require('./101-main.js');
const UserOccurrenceDict = [];
for (const key in dict) {
  const value = dict[key];
  if (!UserOccurrenceDict[value]) {
    UserOccurrenceDict[value] = [];
  }

  UserOccurrenceDict[value].push(key);
}
