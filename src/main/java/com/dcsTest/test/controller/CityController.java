package com.dcsTest.test.controller;

import com.dcsTest.test.model.CityWeather;
import com.dcsTest.test.repository.CityRepository;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cache.annotation.Cacheable;
import org.springframework.data.domain.Example;
import org.springframework.http.HttpStatus;
import org.springframework.web.bind.annotation.*;

import java.time.Instant;
import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Date;
import java.util.List;
import java.util.Locale;

@RestController
public class CityController {

    private final Logger LOG = LoggerFactory.getLogger(getClass());

    private final CityRepository cityRepository;

    @Autowired
    public CityController(CityRepository cityRepository) {
        this.cityRepository = cityRepository;
    }

//    @GetMapping("/hello")
//    public String hello() {
//        return "Hello, world!";
//    }

    @Cacheable(value = "cityWeathers", key = "#cityName")
    @RequestMapping(value = "/weather/{cityName}", method = RequestMethod.GET)
    public CityWeather getCityWeather(@PathVariable String cityName) {
        LOG.info("Getting weather in the city by name {}.", cityName);

        Example<CityWeather> example = Example.of(new CityWeather(cityName, null, null));
        return cityRepository.findOne(example).orElse(new CityWeather("myCity", "Sun", LocalDate.of(2023,01,01)));
    }

    @RequestMapping(value = "/weather/date/{date}", method = RequestMethod.GET)
    public List<CityWeather> getCityWeathers(@PathVariable String date) {
        LOG.info("Getting all cities and weather status for a date {}", date);
        LocalDate expectedDate = LocalDate.parse(date);
        Example<CityWeather> example = Example.of(new CityWeather(null, null, expectedDate));
        return cityRepository.findAll(example);
    }

    @Cacheable(value = "cityWeathers")
    @RequestMapping(value = "/weather", method = RequestMethod.POST)
    public void createCityWeather(@RequestBody CityWeather cityWeather) {
        LOG.info("Create a cityWeather for city {}", cityWeather);
        cityWeather.setCityName(cityWeather.getCityName().toLowerCase());
        cityRepository.save(cityWeather);
    }

    @GetMapping("/error")
    @ResponseStatus(code = HttpStatus.INTERNAL_SERVER_ERROR, reason = "Internal Server Error")
    public String error() {
        return "Method always return internal server error";
    }
}