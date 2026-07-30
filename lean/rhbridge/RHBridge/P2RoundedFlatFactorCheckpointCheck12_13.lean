import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk13 :
    P2RoundedFactorCheckpointData.panel12FlatEven13 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨13, by decide⟩ := by
  decide +kernel

theorem panel12FlatEven13_eq :
    P2RoundedFactorCheckpointData.panel12FlatEven13 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨13, by decide⟩ := by
  exact panel12FlatComponentChunk13

end RHP2Bridge
