FROM maven:3.8.1-jdk-11

COPY RealTimeSalesAnalytics.java /app/RealTimeSalesAnalytics.java
WORKDIR /app

RUN mvn clean package

CMD ["java", "-cp", "target/RealTimeSalesAnalytics.jar", "RealTimeSalesAnalytics"]