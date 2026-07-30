import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk17 :
    P2RoundedFactorCheckpointData.panel12FlatEven17 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  decide +kernel

theorem panel12FlatEven17_eq :
    P2RoundedFactorCheckpointData.panel12FlatEven17 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨17, by decide⟩ := by
  exact panel12FlatComponentChunk17

end RHP2Bridge
