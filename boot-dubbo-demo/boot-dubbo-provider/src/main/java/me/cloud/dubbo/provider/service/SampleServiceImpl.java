package me.cloud.dubbo.provider.service;

import me.cloud.dubbo.api.SampleService;
import org.apache.dubbo.config.annotation.Service;
import org.springframework.beans.factory.annotation.Value;

@Service(version = "${project.service.version}")
public class SampleServiceImpl implements SampleService {
    @Value("${dubbo.application.name}")
    private String serviceName;

    @Override
    public String sayHi(String name) {
        return String.format("[%s] : Hello, %s", serviceName, name);
    }
}
