import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk0 :
    P2RoundedFactorCheckpointData.panel12FlatEven0 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  decide +kernel

theorem panel12FlatEven0_eq :
    P2RoundedFactorCheckpointData.panel12FlatEven0 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨0, by decide⟩ := by
  exact panel12FlatComponentChunk0

end RHP2Bridge
