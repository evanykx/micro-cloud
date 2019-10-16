package me.cloud.dubbo.consumer;

import me.cloud.dubbo.api.SampleService;
import org.apache.dubbo.config.annotation.Reference;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.boot.ApplicationRunner;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.EnableAutoConfiguration;
import org.springframework.context.annotation.Bean;

@EnableAutoConfiguration
public class ConsumerApp {
    private final Logger logger = LoggerFactory.getLogger(getClass());

    @Reference(version = "${project.service.version}")
    private SampleService sampleService;

    public static void main(String[] args) {
        SpringApplication.run(ConsumerApp.class).close();
    }

    @Bean
    public ApplicationRunner runner(){
        return args -> logger.info(sampleService.sayHi("mercylitz"));
    }
}
