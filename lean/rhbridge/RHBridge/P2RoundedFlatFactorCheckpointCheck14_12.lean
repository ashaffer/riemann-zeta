import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk12 :
    P2RoundedFactorCheckpointData.panel14FlatEven12 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  decide +kernel

theorem panel14FlatEven12_eq :
    P2RoundedFactorCheckpointData.panel14FlatEven12 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨12, by decide⟩ := by
  exact panel14FlatComponentChunk12

end RHP2Bridge
