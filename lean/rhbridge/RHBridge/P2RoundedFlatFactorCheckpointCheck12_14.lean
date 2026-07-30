import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk14 :
    P2RoundedFactorCheckpointData.panel12FlatEven14 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  decide +kernel

theorem panel12FlatEven14_eq :
    P2RoundedFactorCheckpointData.panel12FlatEven14 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨14, by decide⟩ := by
  exact panel12FlatComponentChunk14

end RHP2Bridge
