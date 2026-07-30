import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk1 :
    P2RoundedFactorCheckpointData.panel31Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix4_eq :
    P2RoundedFactorCheckpointData.panel31Prefix4 =
      normalizedPrefixTermAtomApprox ⟨4, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk1.1

theorem panel31Prefix5_eq :
    P2RoundedFactorCheckpointData.panel31Prefix5 =
      normalizedPrefixTermAtomApprox ⟨5, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk1.2.1

theorem panel31Prefix6_eq :
    P2RoundedFactorCheckpointData.panel31Prefix6 =
      normalizedPrefixTermAtomApprox ⟨6, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk1.2.2.1

theorem panel31Prefix7_eq :
    P2RoundedFactorCheckpointData.panel31Prefix7 =
      normalizedPrefixTermAtomApprox ⟨7, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk1.2.2.2

end RHP2Bridge
