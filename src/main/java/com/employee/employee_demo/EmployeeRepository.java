package com.employee.employee_demo;

import org.springframework.data.cassandra.repository.Query;
import org.springframework.data.repository.CrudRepository;

public interface EmployeeRepository extends CrudRepository<Employee, Integer> {

	@Query("select * from employee where id =?0")
	public Employee findById(int id);

	/*
	 * @Query("select * from employee where age >?0") public List<Employee>
	 * findEmployeeHasAgeGreaterThan(int age);
	 */
}
