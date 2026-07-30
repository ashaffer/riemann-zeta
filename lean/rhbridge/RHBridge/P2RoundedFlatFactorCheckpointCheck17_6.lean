import RHBridge.P2RoundedFlatFactorCheckpointData17

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel17FlatComponentChunk6 :
    P2RoundedFactorCheckpointData.panel17FlatEven6 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel17FlatEven6_eq :
    P2RoundedFactorCheckpointData.panel17FlatEven6 =
      (P2RoundedFactorCheckpointData.panel17TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  exact panel17FlatComponentChunk6

end RHP2Bridge
