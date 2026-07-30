import RHBridge.P2RoundedFactorCheckpointData12

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel12FactorChunk1 :
    P2RoundedFactorCheckpointData.panel12Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨12, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel12Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨12, by decide⟩ := by
  decide +kernel

theorem panel12Prefix4_eq :
    P2RoundedFactorCheckpointData.panel12Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk1.1

theorem panel12Prefix5_eq :
    P2RoundedFactorCheckpointData.panel12Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk1.2.1

theorem panel12Prefix6_eq :
    P2RoundedFactorCheckpointData.panel12Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk1.2.2.1

theorem panel12Prefix7_eq :
    P2RoundedFactorCheckpointData.panel12Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨12, by decide⟩ := by
  exact panel12FactorChunk1.2.2.2

end RHP2Bridge
