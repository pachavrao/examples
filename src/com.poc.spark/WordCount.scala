package com.poc.spark

import org.apache.log4j.Level
import org.apache.log4j.Logger
import org.apache.spark.SparkConf
import org.apache.spark.SparkContext

object WordCount {

  def main(args: Array[String]) {

    Logger.getLogger("org").setLevel(Level.ERROR)
    val conf = new SparkConf().setAppName("wordCounts").setMaster("local[3]")
    val sc = new SparkContext(conf)

    var a =10
     a = 10
    a = a
    val all_lines = sc.textFile("in/word_count.text")
    val words = all_lines.flatMap(line => line.split(" "))

    val wordCounts = words.countByValue()
    for ((word, count) <- wordCounts) println(word + " : " + count)
  }
}
