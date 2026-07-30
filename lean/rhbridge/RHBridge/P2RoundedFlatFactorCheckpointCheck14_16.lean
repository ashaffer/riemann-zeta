import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk16 :
    P2RoundedFactorCheckpointData.panel14FlatEven16 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  decide +kernel

theorem panel14FlatEven16_eq :
    P2RoundedFactorCheckpointData.panel14FlatEven16 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨16, by decide⟩ := by
  exact panel14FlatComponentChunk16

end RHP2Bridge
