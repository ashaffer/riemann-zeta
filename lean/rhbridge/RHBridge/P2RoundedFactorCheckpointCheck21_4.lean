import RHBridge.P2RoundedFactorCheckpointData21

namespace RHP2Bridge

open P2RoundedCanonical
open P2RoundedSharedEvaluator

set_option maxRecDepth 100000
set_option maxHeartbeats 50000000

theorem panel21FactorChunk4 :
    P2RoundedFactorCheckpointData.panel21Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨21, by decide⟩ ∧
      P2RoundedFactorCheckpointData.panel21Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨21, by decide⟩ := by
  decide +kernel

theorem panel21Prefix16_eq :
    P2RoundedFactorCheckpointData.panel21Prefix16 =
      normalizedPrefixTermAtomApprox ⟨16, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk4.1

theorem panel21Prefix17_eq :
    P2RoundedFactorCheckpointData.panel21Prefix17 =
      normalizedPrefixTermAtomApprox ⟨17, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk4.2.1

theorem panel21Prefix18_eq :
    P2RoundedFactorCheckpointData.panel21Prefix18 =
      normalizedPrefixTermAtomApprox ⟨18, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk4.2.2.1

theorem panel21Prefix19_eq :
    P2RoundedFactorCheckpointData.panel21Prefix19 =
      normalizedPrefixTermAtomApprox ⟨19, by decide⟩ ⟨21, by decide⟩ := by
  exact panel21FactorChunk4.2.2.2

end RHP2Bridge
