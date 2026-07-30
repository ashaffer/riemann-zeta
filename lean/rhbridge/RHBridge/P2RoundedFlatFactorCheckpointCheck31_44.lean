import RHBridge.P2RoundedFlatFactorCheckpointData31

namespace RHP2Bridge

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FlatComponentChunk44 :
    P2RoundedFactorCheckpointData.panel31FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨20, by decide⟩ := by
  decide +kernel

theorem panel31FlatOdd20_eq :
    P2RoundedFactorCheckpointData.panel31FlatOdd20 =
      (P2RoundedFactorCheckpointData.panel31TruncatedOddComponents).get ⟨20, by decide⟩ := by
  exact panel31FlatComponentChunk44

end RHP2Bridge
