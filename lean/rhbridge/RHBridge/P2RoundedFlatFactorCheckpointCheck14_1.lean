import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk1 :
    P2RoundedFactorCheckpointData.panel14FlatEven1 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  decide +kernel

theorem panel14FlatEven1_eq :
    P2RoundedFactorCheckpointData.panel14FlatEven1 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨1, by decide⟩ := by
  exact panel14FlatComponentChunk1

end RHP2Bridge
