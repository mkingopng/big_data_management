# https://www.edureka.co/blog/install-hadoop-single-node-hadoop-cluster
# https://hadoop.apache.org/docs/stable/hadoop-project-dist/hadoop-common/SingleCluster.html
# https://medium.com/@hema-chandra/cannot-execute-libexec-hdfs-config-sh-ec7c3b1a45bd

# 1) download the java tar file

# 2) extract the java tar file

# 3) check that java is installed
java --version

# download the latest hadoop version (currently 3.3.3)
https://www.apache.org/dyn/closer.cgi/hadoop/common/

# move the hadoop tar file to home folder & extract 
tar -xvf hadoop-3.3.3.tar.gz
# or
sudo tar -xzvf hadoop-3.3.3.tar.gz

# check that hadoop is now installed
hadoop --version

# check the paths for java
update-alternatives --config java  # This works best

# this is my JAVA_HOME
JAVA_HOME="/usr/lib/jvm/java-18-openjdk-amd64/bin/java"

echo $JAVA_HOME # this returns the correct path once you update alternatives & force restart

# hadoop
echo $HADOOP_HOME

# my HADOOP_HOME
HADOOP_HOME="/home/hadoop-inst"

# add the hadoop and java paths in the bash file (.bashrc)
# apply the changes to the current terminal
source .bashrc

# by default hadoop is configured for stand along operation
# follow these steps to configure for pseudo-distributed operation


# edit the hadoop configuration files

	# Edit core-site.xml configuration tag
	<?xml version="1.0" encoding="UTF-8"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	<configuration>
    	<property>
        	<name>fs.defaultFS</name>
        	<value>hdfs://localhost:9000</value>
    	</property>
	</configuration>
	
	# Edit hdfs-site.xml configuration tag
	<?xml version="1.0" encoding="UTF-8"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	<configuration>
    	<property>
        	<name>dfs.replication</name>
        	<value>1</value>
    	</property>
	</configuration>
	
# setup Setup passphraseless ssh
	# 1) check that you can ssh to the localhost without a paraphrase
	ssh localhost

	# 2) if you cannot then execute the following commands:
	ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa
	cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys
	chmod 0600 ~/.ssh/authorized_keys

	# 3) repeat
	ssh localhost

# muthafucker!!!!

# Execution
cd hadoop-inst

	# 1) format the file system
	bin/hdfs namenode -format

	# 2) start the NameNode daemon and DataNode daemon
	sbin/start-dfs.sh

	# 3) Browse the web interface for the NameNode; by default it is available at:
	http://localhost:9870/

	# 4) Make the HDFS directories required to execute MapReduce jobs:
	bin/hdfs dfs -mkdir /user
	bin/hdfs dfs -mkdir /user/<username>

	# 5) Copy the input files into the distributed filesystem:
	bin/hdfs dfs -mkdir input
	bin/hdfs dfs -put etc/hadoop/*.xml input

	# 6) Run some of the examples provided:
	bin/hadoop jar share/hadoop/mapreduce/hadoop-mapreduce-examples-3.3.3.jar grep input output 'dfs[a-z.]+'

	#7) Examine the output files: Copy the output files from the distributed filesystem to the local filesystem and examine them:
	bin/hdfs dfs -get output output
	cat output/*

	# or view the output files on the distributed filesystem:
	bin/hdfs dfs -cat output/*

	# 8) When you’re done, stop the daemons with:
	sbin/stop-dfs.sh

# if you want to run a MapReduce job on Yarn on in a pseudo-distributed mode
# you need to set a few parameters

	# 1) Edit mapred-site.xml configuration tag
	/home/hadoop-3.3.3/etc/hadoop/mapred-site.xml:

	<?xml version="1.0" encoding="UTF-8"?>
	<?xml-stylesheet type="text/xsl" href="configuration.xsl"?>
	<configuration>
	    <property>
        	<name>mapreduce.framework.name</name>
        	<value>yarn</value>
    	</property>
    	<property>
        	<name>mapreduce.application.classpath</name>
        	<value>$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/*:$HADOOP_MAPRED_HOME/share/hadoop/mapreduce/lib/*</value>
    	</property>
	</configuration>
	
	# Edit yarn-site.xml configuration tag
	/home/hadoop-3.3.3/etc/hadoop/yarn-site.xml:

	<?xml version="1.0">
	<configuration>
		<property>
        	<name>yarn.nodemanager.aux-services</name>
        	<value>mapreduce_shuffle</value>
    	</property>
    	<property>
        	<name>yarn.nodemanager.env-whitelist</name>
        	<value>JAVA_HOME,HADOOP_COMMON_HOME,HADOOP_HDFS_HOME,HADOOP_CONF_DIR,CLASSPATH_PREPEND_DISTCACHE,HADOOP_YARN_HOME,HADOOP_HOME,PATH,LANG,TZ,HADOOP_MAPRED_HOME</value>
    	</property>
	</configuration>

	# Start ResourceManager daemon and NodeManager daemon:
	sbin/start-yarn.sh

	# Browse the web interface for the ResourceManager; by default it is available at:
	http://localhost:8088/

	# run a MapReduce job

	# when you're done, stop the daemons with
	sbin/stop-yarn.sh


# -------------------------

	# Edit hadoop-env.sh and add the JAVA_HOME path
	JAVA_HOME=/usr/lib/jvm/jdk-18

	# go to the hadoop home directory and format the NameNode
	cd hadoop-3.3.3
	bin/hadoop namenode -format

# go to the hadoop-3.3.3 directory and start all the daemons
cd hadoop-3.3.3
./start-all.sh

	# or 
	start-dfs.sh
	start-yarn.sh
	mr-jobhistory-daemon.sh

	# start NameNode
	./hadoop-daemon.sh start namenode

	# start data Node
	./hadoop-daemon.sh start datanode

	# start resource manager
	./yarn-daemon.sh start resourcemanager

	# start NodeManager
	./yarn-daemon.sh start nodemanager

	# start JobHistoryServer
	./mr-jobhistory-daemon.sh start historyserver

# 14) to check that all the hadoop services are running
jps

# 15) open your browser and go to 
localhost:50070/dfshealth.html