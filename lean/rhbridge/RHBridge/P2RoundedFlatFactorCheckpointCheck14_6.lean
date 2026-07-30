import RHBridge.P2RoundedFlatFactorCheckpointData14

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FlatComponentChunk6 :
    P2RoundedFactorCheckpointData.panel14FlatEven6 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel14FlatEven6_eq :
    P2RoundedFactorCheckpointData.panel14FlatEven6 =
      (P2RoundedFactorCheckpointData.panel14TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  exact panel14FlatComponentChunk6

end RHP2Bridge
