import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk15 :
    P2RoundedFactorCheckpointData.panel12Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix60_eq :
    P2RoundedFactorCheckpointData.panel12Prefix60 =
      normalizedPrefixTermAtomApprox ⟨60, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk15.1

theorem panel12Prefix61_eq :
    P2RoundedFactorCheckpointData.panel12Prefix61 =
      normalizedPrefixTermAtomApprox ⟨61, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk15.2.1

theorem panel12Prefix62_eq :
    P2RoundedFactorCheckpointData.panel12Prefix62 =
      normalizedPrefixTermAtomApprox ⟨62, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk15.2.2.1

theorem panel12Prefix63_eq :
    P2RoundedFactorCheckpointData.panel12Prefix63 =
      normalizedPrefixTermAtomApprox ⟨63, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk15.2.2.2

end RHP2Bridge
