package com.dcsTest.test.model;

import jakarta.persistence.*;

import java.io.Serializable;
import java.time.LocalDate;
import java.util.Date;

@Entity
public class CityWeather implements Serializable {

    private static final long serialVersionUID = 7156526077883281623L;

    @Id
    @SequenceGenerator(name = "SEQ_GEN", sequenceName = "SEQ_CITY", allocationSize = 1)
    @GeneratedValue(strategy = GenerationType.SEQUENCE, generator = "SEQ_GEN")
    private Long id;
    private String cityName;
    private String weather;

    private LocalDate date;

    public CityWeather() {
    }

    public CityWeather(String cityName, String weather, LocalDate date) {
        this.cityName = cityName;
        this.weather = weather;
        this.date = date;
    }

    @Override
    public String toString() {
        return String.format("City{id=%d, name='%s'} Weather{weather='%s'} Date{date='%s'}", id, cityName, weather, date);
    }

    public Long getId() {
        return this.id;
    }

    public String getCityName() {
        return this.cityName;
    }

    public void setCityName(String cityName) {
        this.cityName = cityName;
    }

    public String getWeather() {
        return this.weather;
    }

    public void setWeather(String weather) {
        this.weather = weather;
    }

    public LocalDate getDate() {
        return this.date;
    }

    public void setDate(LocalDate date) {
        this.date = date;
    }
}

