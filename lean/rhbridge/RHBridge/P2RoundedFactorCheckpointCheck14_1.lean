import RHBridge.P2RoundedFactorCheckpointData14

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel14FactorChunk1 :
    P2RoundedFactorCheckpointData.panel14Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨14, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel14Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨14, by decide⟩ := by
  decide +kernel

theorem panel14Prefix4_eq :
    P2RoundedFactorCheckpointData.panel14Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk1.1

theorem panel14Prefix5_eq :
    P2RoundedFactorCheckpointData.panel14Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk1.2.1

theorem panel14Prefix6_eq :
    P2RoundedFactorCheckpointData.panel14Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk1.2.2.1

theorem panel14Prefix7_eq :
    P2RoundedFactorCheckpointData.panel14Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨14, by decide⟩ := by
  exact panel14FactorChunk1.2.2.2

end RHP2Bridge
