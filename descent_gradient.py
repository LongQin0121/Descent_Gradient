import math

def calculate_descent_gradient(ias_knots, weight_kg, cd, wing_area_m2, idle_thrust_n):
    """
    计算飞机等表速下降梯度（所有参数均为输入变量）
    
    Args:
        ias_knots: 表速 (节)
        weight_kg: 飞机重量 (kg) 
        cd: 阻力系数
        wing_area_m2: 机翼面积 (m²)
        idle_thrust_n: IDLE推力 (N)
        
    Returns:
        dict: 包含所有计算结果的字典
    """
    # 常数
    RHO_0 = 1.225  # 标准海平面空气密度 kg/m³
    KNOTS_TO_MS = 0.5144  # 节转米/秒的转换因子
    G = 9.8  # 重力加速度
    
    # 步骤1: 速度转换
    ias_ms = ias_knots * KNOTS_TO_MS
    
    # 步骤2: 计算动压
    dynamic_pressure = 0.5 * RHO_0 * ias_ms**2
    
    # 步骤3: 计算阻力
    drag_force = dynamic_pressure * wing_area_m2 * cd
    
    # 步骤4: 计算净阻力（阻力 - IDLE推力）
    net_drag = drag_force - idle_thrust_n
    
    # 步骤5: 计算重量（牛顿）
    weight_n = weight_kg * G
    
    # 步骤6: 计算下降梯度
    descent_gradient = net_drag / weight_n
    
    # 步骤7: 计算下降角
    if descent_gradient > 1.0:
        descent_angle_rad = math.pi/2  # 90度最大值
        descent_angle_deg = 90.0
    elif descent_gradient <= 0:
        descent_angle_rad = 0.0
        descent_angle_deg = 0.0
    else:
        descent_angle_rad = math.asin(descent_gradient)
        descent_angle_deg = math.degrees(descent_angle_rad)
    
    # 步骤8: 计算下降梯度比
    if descent_gradient > 0:
        descent_ratio = 1.0 / descent_gradient
    else:
        descent_ratio = float('inf')
    
    # 返回完整结果
    results = {
        # 输入参数
        'ias_knots': ias_knots,
        'ias_ms': ias_ms,
        'weight_kg': weight_kg,
        'weight_n': weight_n,
        'cd': cd,
        'wing_area_m2': wing_area_m2,
        'idle_thrust_n': idle_thrust_n,
        
        # 中间计算结果
        'dynamic_pressure_pa': dynamic_pressure,
        'drag_force_n': drag_force,
        'net_drag_n': net_drag,
        
        # 最终结果
        'descent_gradient': descent_gradient,
        'descent_angle_rad': descent_angle_rad,
        'descent_angle_deg': descent_angle_deg,
        'descent_ratio': descent_ratio,
        
        # 状态检查
        'is_valid_descent': net_drag > 0
    }
    
    return results

def print_results(results):
    """格式化打印计算结果"""
    print("=" * 60)
    print("飞机下降梯度计算结果")
    print("=" * 60)
    
    print("输入参数:")
    print(f"  表速 (IAS):        {results['ias_knots']} 节 ({results['ias_ms']:.2f} m/s)")
    print(f"  飞机重量:          {results['weight_kg']:,} kg ({results['weight_n']:,.0f} N)")
    print(f"  阻力系数 (CD):     {results['cd']}")
    print(f"  机翼面积:          {results['wing_area_m2']} m²")
    print(f"  IDLE推力:          {results['idle_thrust_n']:,.0f} N")
    
    print("\n中间计算:")
    print(f"  动压:              {results['dynamic_pressure_pa']:,.0f} Pa")
    print(f"  阻力:              {results['drag_force_n']:,.0f} N")
    print(f"  净阻力:            {results['net_drag_n']:,.0f} N")
    
    print("\n最终结果:")
    if results['is_valid_descent']:
        print(f"  下降梯度:          {results['descent_gradient']:.4f}")
        print(f"  下降角:            {results['descent_angle_deg']:.2f}° ({results['descent_angle_rad']:.4f} rad)")
        print(f"  下降梯度比:        1:{results['descent_ratio']:.1f}")
    else:
        print("  警告: IDLE推力大于或等于阻力，无法维持稳定下降！")
    
    print("=" * 60)

def calculate_multiple_cases(cases):
    """批量计算多个案例"""
    print("批量计算结果:")
    print("=" * 100)
    print(f"{'IAS(节)':<8} {'重量(kg)':<10} {'CD':<6} {'面积(m²)':<10} {'IDLE(N)':<10} {'下降梯度':<12} {'下降角(°)':<12} {'下降比':<12}")
    print("-" * 100)
    
    for case in cases:
        result = calculate_descent_gradient(
            case['ias'], case['weight'], case['cd'], 
            case['wing_area'], case['idle_thrust']
        )
        
        if result['is_valid_descent']:
            print(f"{case['ias']:<8} {case['weight']:<10,} {case['cd']:<6} {case['wing_area']:<10} "
                  f"{case['idle_thrust']:<10,} {result['descent_gradient']:<12.4f} "
                  f"{result['descent_angle_deg']:<12.2f} 1:{result['descent_ratio']:<11.1f}")
        else:
            print(f"{case['ias']:<8} {case['weight']:<10,} {case['cd']:<6} {case['wing_area']:<10} "
                  f"{case['idle_thrust']:<10,} {'无法下降':<12} {'N/A':<12} {'N/A':<12}")

# 使用示例
if __name__ == "__main__":
    # 单个计算示例
    print("单个计算示例:")
    result = calculate_descent_gradient(
        ias_knots=300,      # 表速 300节
        weight_kg=64500,    # 重量 64,500kg
        cd=0.023,           # 阻力系数 0.023
        wing_area_m2=122.6, # 机翼面积 122.6m²
        idle_thrust_n=8000  # IDLE推力 8,000N
    )
    print_results(result)
    
    print("\n\n")
    
    # 批量计算示例
    test_cases = [
        {'ias': 250, 'weight': 64500, 'cd': 0.023, 'wing_area': 122.6, 'idle_thrust': 8000},
        {'ias': 300, 'weight': 64500, 'cd': 0.023, 'wing_area': 122.6, 'idle_thrust': 8000},
        {'ias': 330, 'weight': 64500, 'cd': 0.023, 'wing_area': 122.6, 'idle_thrust': 8000},
        {'ias': 300, 'weight': 64500, 'cd': 0.023, 'wing_area': 122.6, 'idle_thrust': 15000},  # 海平面
        {'ias': 300, 'weight': 64500, 'cd': 0.023, 'wing_area': 122.6, 'idle_thrust': 4000},   # 高空
        {'ias': 300, 'weight': 58050, 'cd': 0.027, 'wing_area': 122.6, 'idle_thrust': 8000},   # 不同重量CD
    ]
    
    calculate_multiple_cases(test_cases)
    
    print("\n\n简单使用示例:")
    print("# 计算单个案例")
    print("result = calculate_descent_gradient(300, 64500, 0.023, 122.6, 8000)")
    print("print(f'下降梯度: {result[\"descent_gradient\"]:.4f}')")
    print("print(f'下降角: {result[\"descent_angle_deg\"]:.2f}°')")