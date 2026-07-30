import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk2 :
    P2RoundedFactorCheckpointData.panel14FlatEven2 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  decide +kernel

theorem panel14FlatEven2_eq :
    P2RoundedFactorCheckpointData.panel14FlatEven2 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨2, by decide⟩ := by
  exact panel14FlatComponentChunk2

end RHP2Bridge
