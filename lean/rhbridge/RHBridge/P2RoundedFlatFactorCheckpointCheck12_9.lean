import RHBridge.P2RoundedFlatFactorCheckpointData12

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FlatComponentChunk9 :
    P2RoundedFactorCheckpointData.panel12FlatEven9 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  decide +kernel

theorem panel12FlatEven9_eq :
    P2RoundedFactorCheckpointData.panel12FlatEven9 =
      (P2RoundedFactorCheckpointData.panel12TruncatedEvenComponents).get ⟨9, by decide⟩ := by
  exact panel12FlatComponentChunk9

end RHP2Bridge
