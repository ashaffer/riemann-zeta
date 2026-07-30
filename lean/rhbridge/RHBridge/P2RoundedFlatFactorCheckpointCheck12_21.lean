import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk21 :
    P2RoundedFactorCheckpointData.panel12FlatEven21 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  decide +kernel

theorem panel12FlatEven21_eq :
    P2RoundedFactorCheckpointData.panel12FlatEven21 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨21, by decide⟩ := by
  exact panel12FlatComponentChunk21

end RHP2Bridge
