package com.dcsTest.test;

import com.dcsTest.test.repository.CityRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.cache.annotation.EnableCaching;

@SpringBootApplication
@EnableCaching
public class DemoApplication {

	private final CityRepository cityRepository;

	private final Logger LOG = LoggerFactory.getLogger(getClass());

	@Autowired
	public DemoApplication(CityRepository cityRepository) {
		this.cityRepository = cityRepository;
	}

	public static void main(String[] args) {
		SpringApplication.run(DemoApplication.class, args);
	}
}