## This is our worker file. We will simulate a very heavy, sequential stochastic process (like a random walk or Monte Carlo simulation) where Python usually struggles because it cannot be easily vectorized into a single matrix multiplication.

# physics_engine.jl
# This is pure Julia code.

module PhysicsEngine

export simulate_heavy_stochastic_process

"""
Simulates a heavy sequential process. 
(e.g., a custom Monte Carlo random walk that cannot be easily vectorized).
"""
function simulate_heavy_stochastic_process(steps::Int, initial_state::Float64)
    state = initial_state
    
    # Julia compiles this loop down to raw machine code.
    # In Python, a loop of 100,000,000 would take several seconds.
    # Here, it takes milliseconds.
    for i in 1:steps
        # Some custom, non-linear stochastic update
        noise = rand() - 0.5
        state = sin(state + noise)
    end
    
    return state
end

end # module