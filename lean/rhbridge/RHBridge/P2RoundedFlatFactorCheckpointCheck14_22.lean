import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk22 :
    P2RoundedFactorCheckpointData.panel14FlatEven22 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  decide +kernel

theorem panel14FlatEven22_eq :
    P2RoundedFactorCheckpointData.panel14FlatEven22 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨22, by decide⟩ := by
  exact panel14FlatComponentChunk22

end RHP2Bridge
