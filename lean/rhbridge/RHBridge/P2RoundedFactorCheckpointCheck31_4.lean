import RHBridge.P2RoundedFactorCheckpointData31

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel31FactorChunk4 :
    P2RoundedFactorCheckpointData.panel31Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨31, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel31Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨31, by decide⟩ := by
  decide +kernel

theorem panel31Prefix16_eq :
    P2RoundedFactorCheckpointData.panel31Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk4.1

theorem panel31Prefix17_eq :
    P2RoundedFactorCheckpointData.panel31Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk4.2.1

theorem panel31Prefix18_eq :
    P2RoundedFactorCheckpointData.panel31Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk4.2.2.1

theorem panel31Prefix19_eq :
    P2RoundedFactorCheckpointData.panel31Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨31, by decide⟩ := by
  exact panel31FactorChunk4.2.2.2

end RHP2Bridge
