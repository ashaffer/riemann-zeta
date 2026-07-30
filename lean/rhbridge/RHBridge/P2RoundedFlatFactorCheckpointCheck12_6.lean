import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk6 :
    P2RoundedFactorCheckpointData.panel12FlatEven6 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  decide +kernel

theorem panel12FlatEven6_eq :
    P2RoundedFactorCheckpointData.panel12FlatEven6 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨6, by decide⟩ := by
  exact panel12FlatComponentChunk6

end RHP2Bridge
