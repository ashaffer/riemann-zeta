import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk14 :
    P2RoundedFactorCheckpointData.panel14FlatEven14 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14FlatEven14_eq :
    P2RoundedFactorCheckpointData.panel14FlatEven14 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  exact panel14FlatComponentChunk14

end RHP2Bridge
