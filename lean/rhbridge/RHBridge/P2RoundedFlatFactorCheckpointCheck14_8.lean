import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk8 :
    P2RoundedFactorCheckpointData.panel14FlatEven8 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  decide +kernel

theorem panel14FlatEven8_eq :
    P2RoundedFactorCheckpointData.panel14FlatEven8 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨8, by decide⟩ := by
  exact panel14FlatComponentChunk8

end RHP2Bridge
